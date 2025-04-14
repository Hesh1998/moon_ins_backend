INSERT INTO tdb.branch (branch_id, branch_name)
VALUES 
  ('B001', 'New York'),
  ('B002', 'Texas');

INSERT INTO tdb.team (team_id, team_name, branch_id)
VALUES 
  ('T001', 'Alpha Sales Team', 'B001'),
  ('T002', 'Beta Sales Team', 'B002');

INSERT INTO tdb.insurance_product (product_id, product_name, product_type, target)
VALUES
  ('P001', 'Life Shield', 'Term Insurance', 100000),
  ('P002', 'Health Plus', 'Health Insurance', 200000),
  ('P003', 'Wealth Builder', 'Investment Plan', 50000),
  ('P004', 'Family Cover', 'Whole Life Insurance', 150000);