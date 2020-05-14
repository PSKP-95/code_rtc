# Code - RTC
## Installation & Information
You can find this [here](https://github.com/PSKP-95/code_rtc/wiki/Installation)
## To Do
- [x] Creating Code
- [x] Running Code on user input
- [x] Creating Testcases
- [x] Running on Testcases
- [x] File explorer
- [x] Context menu for File explorer with delete, cut, rename, paste.
- [x] Export files
- [ ] Import Folders/Files

## Testing
This application is tensted on Ubuntu 19.10 with Firefox

## mysql and sqlite3
Need to just change `DATABASE` in `code_rtc/backend/src/db.py`
- mysql : for mysql / mariadb
- sqlite3 : for sqlite3 

## Schema for Sqlite3
### for bucket
`CREATE TABLE bucket (
  node_id integer PRIMARY KEY AUTOINCREMENT,
  type int(2) NOT NULL,
  node varchar(50) NOT NULL,
  file text,
  parent int(11) NOT NULL, 
  flag integer,
  note text);`

### for tests

`CREATE TABLE tests (
  test_id integer PRIMARY KEY AUTOINCREMENT,
  type int(1) NOT NULL,
  input text NOT NULL,
  output text NOT NULL,
  node_id int(11) NOT NULL,
  status int(11) NOT NULL DEFAULT '0',
  CONSTRAINT fk_node
    FOREIGN KEY (node_id)
    REFERENCES bucket(node_id)
);`

## Demo

See Video on Youtube https://www.youtube.com/watch?v=QwXDyiKYOas