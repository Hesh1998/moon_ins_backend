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

INSERT INTO tdb.sale (sale_id, sale_date, agent_id, product_id, amount)
VALUES
  -- Sales for P001 (Target: 100000) → Hits target
  ('S001', '2025-04-01', 'A001', 'P001', 30000),
  ('S002', '2025-04-02', 'A002', 'P001', 40000),
  ('S003', '2025-04-03', 'A005', 'P001', 30000),

  -- Sales for P002 (Target: 50000) → Below target
  ('S004', '2025-04-01', 'A004', 'P002', 15000),
  ('S005', '2025-04-02', 'A007', 'P002', 10000),

  -- Sales for P003 (Target: 150000) → Hits target
  ('S006', '2025-04-01', 'A002', 'P003', 60000),
  ('S007', '2025-04-02', 'A004', 'P003', 50000),
  ('S008', '2025-04-03', 'A006', 'P003', 40000),

  -- Sales for P004 (Target: 120000) → Below target
  ('S009', '2025-04-03', 'A003', 'P004', 20000),
  ('S010', '2025-04-04', 'A008', 'P004', 30000);