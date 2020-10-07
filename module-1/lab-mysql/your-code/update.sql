SET SQL_SAFE_UPDATES = 0;
UPDATE lab_mysql_apf.salespersons
SET sp_store = 'Miami'
WHERE sp_name = 'Paige Turner';

UPDATE lab_mysql_apf.customers
SET cmr_email = 'ppicasso@gmail.com'
WHERE cmr_name = 'Pablo Picasso';

UPDATE lab_mysql_apf.customers
SET cmr_email = 'lincoln@us.gov'
WHERE cmr_name = 'Abraham Lincoln';

UPDATE lab_mysql_apf.customers
SET cmr_email = 'hello@napoleon.me'
WHERE cmr_name = 'Napoléon Bonaparte';