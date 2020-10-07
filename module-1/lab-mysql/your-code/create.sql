USE lab_mysql_apf;
DROP TABLE IF EXISTS invoices;
DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS salespersons;

CREATE TABLE cars
(
ID INT,
c_vin VARCHAR(20),
c_manufacturer VARCHAR(15),
c_model VARCHAR(20),
c_year YEAR,
c_color VARCHAR(10),
PRIMARY KEY (ID)
);

CREATE TABLE customers
(
ID INT PRIMARY KEY,
cmr_customer_id INT,
cmr_name VARCHAR(20),
cmr_phone VARCHAR(20),
cmr_email VARCHAR(35),
cmr_address VARCHAR(50),
cmr_city VARCHAR(15),
cmr_state VARCHAR(15),
cmr_country VARCHAR(15),
cmr_cp VARCHAR(7)
);

CREATE TABLE salespersons
(
ID INT,
sp_staff_id INT,
sp_name VARCHAR(15),
sp_store VARCHAR(15),
PRIMARY KEY (ID)
);

CREATE TABLE invoices
(
ID INT,
i_number INT,
i_date DATE,
i_car INT,
i_customer_id INT,
i_staff_id INT,
CONSTRAINT invoice_vin FOREIGN KEY (i_car) REFERENCES cars(ID),
CONSTRAINT invoice_customer_id FOREIGN KEY (i_customer_id) REFERENCES customers(ID),
CONSTRAINT invoice_staff_id FOREIGN KEY (i_staff_id) REFERENCES salespersons(ID),
PRIMARY KEY (ID)
);