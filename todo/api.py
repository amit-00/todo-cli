import pathlib
import io
import csv
import os
import uuid

class Api:

  def save_todo(self, todo):
    try:
      res = []

      with open(self.file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        id = uuid.uuid4()
        res = [id] + todo + [0] + [1.0]
        writer.writerow(res)
      
      return {'data': res, 'status': 200}
    except:
       print(f'Error saving todo')
       return {'data': [], 'status': 500}
    
  def update_todo(self, id, todos):
    temp_file = os.path.join(self.path, 'temp.csv')
    try:
      res = []

      with open(self.file_path, 'r', newline='') as infile, open(temp_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
          if row[0] == id:
            res = [id] + todos + [row[4]] + [float(row[5]) + 1.0]
            writer.writerow(res)
            continue

          writer.writerow(row)

      os.replace(temp_file, self.file_path)
      
      return {'data': res, 'status': 200}
    except:
      print('Error saving todo')
      if os.path.exists(temp_file):
        os.remove(temp_file)
        print(f"File '{temp_file}' deleted successfully.")
      return {'data': [], 'status': 500}
    
  def mark_completed(self, id):
    temp_file = os.path.join(self.path, 'temp.csv')
    try:
      res = []

      with open(self.file_path, 'r', newline='') as infile, open(temp_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
          if row[0] == id:
            res = row
            res[4] = 1
            writer.writerow(res)
            continue

          writer.writerow(row)

      os.replace(temp_file, self.file_path)
      
      return {'data': res, 'status': 200}
    except:
      print('Error saving todo')
      if os.path.exists(temp_file):
        os.remove(temp_file)
        print(f"File '{temp_file}' deleted successfully.")
      return {'data': [], 'status': 500}
    
  def remove_todo(self, id):
    try:
      res = []
      temp_file = os.path.join(self.path, 'temp.csv')

      with open(self.file_path, 'r', newline='') as infile, open(temp_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
          if row[0] == id:
            res = row
            continue

          writer.writerow(row)

      os.replace(temp_file, self.file_path)
      
      return {'data': res, 'status': 200}
    except:
       print(f'Error saving todo')
       return {'data': [], 'status': 500}
    
  def get_todos(self, priority):
    try:
      res = []
      with open(self.file_path, 'r', newline='') as infile:
        reader = csv.reader(infile)

        for row in reader:
          if not priority:
            res.append(row)
          elif row[3] == priority:
            res.append(row)
      
      if not priority:
        res.pop(0)

      return {'data': res, 'status': 200}
    except:
      print('Error listing todos')
      return {'data': [], 'status': 500}

  def __init__(self):
    self.path = pathlib.Path(__file__).parent.resolve()
    self.file_path = os.path.join(self.path, 'todos.csv')

    if os.path.isfile(self.file_path) and os.access(self.file_path, os.R_OK):
        # checks if file exists
        print ("Save file exists and is readable")
    else:
        print ("Either save file is missing or is not readable, creating new save file...")
        with io.open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            field = ['Id', 'Title', 'Description', 'Priority', 'IsComplete', 'Version']

            writer.writerow(field)

if __name__ == "__main__":

  api = Api()
  res = api.get_todos('m')

  print(res)
