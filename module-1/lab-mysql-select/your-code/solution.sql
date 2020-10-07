USE publications;
/*-----------CHALLENGE 1----------------*/
SELECT authors.au_id AS 'AUTHOR ID',
authors.au_lname AS 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
titles.title AS 'TITLE',
publishers.pub_name AS 'PUBLISHER'
FROM authors
JOIN titleauthor
ON authors.au_id = titleauthor.au_id
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN publishers
ON titles.pub_id = publishers.pub_id
ORDER BY authors.au_id;

/*-----------CHALLENGE 2----------------*/
SELECT authors.au_id AS 'AUTHOR ID',
authors.au_lname AS 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
publishers.pub_name AS 'PUBLISHER',
count(titles.title_id) AS 'TITLE COUNT'
FROM authors
JOIN titleauthor
ON authors.au_id = titleauthor.au_id
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN publishers
ON titles.pub_id = publishers.pub_id
GROUP BY authors.au_id, publishers.pub_id
ORDER BY authors.au_id DESC;

/*-----------CHALLENGE 3----------------*/
SELECT authors.au_id AS 'AUTHOR ID',
authors.au_lname AS 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
SUM(titles.ytd_sales) AS 'TOTAL'
FROM authors
LEFT JOIN titleauthor
ON authors.au_id = titleauthor.au_id
LEFT JOIN titles
ON titleauthor.title_id = titles.title_id
GROUP BY authors.au_id
ORDER BY TOTAL DESC /*¿por qué no funciona poner en vez de TOTAL sales.qty o 'TOTAL'?*/
LIMIT 3;

/*-----------CHALLENGE 4----------------*/
SELECT authors.au_id AS 'AUTHOR ID',
authors.au_lname AS 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
COALESCE(SUM(titles.ytd_sales),0) AS 'TOTAL'
FROM authors
LEFT JOIN titleauthor
ON authors.au_id = titleauthor.au_id
LEFT JOIN titles
ON titleauthor.title_id = titles.title_id
GROUP BY authors.au_id
ORDER BY TOTAL DESC;

/*-----------BONUS----------------*/
/*royalties = sales.qty * titles.price * titles.royalty*/
 SELECT step_3.au_id 'AUTHOR ID', step_3.au_lname 'LAST NAME', step_3.au_fname 'FIRST NAME', SUM(step_3.advance + ROYALTIES) 'PROFITS'
 FROM ( SELECT step_2.title_id, step_2.au_id, step_2.au_lname, step_2.au_fname, step_2.advance, SUM(ROYALTY) 'ROYALTIES'
	FROM ( SELECT titles.title_id, authors.au_id, authors.au_lname, authors.au_fname, titles.advance, (titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) 'ROYALTY'
			FROM titles
			JOIN titleauthor ON titles.title_id = titleauthor.title_id
			JOIN sales ON titles.title_id = sales.title_id
			JOIN authors ON titleauthor.au_id = authors.au_id
        ) AS step_2
        GROUP BY au_id, title_id
    ) AS step_3
GROUP BY step_3.au_id
ORDER BY PROFITS DESC
LIMIT 3;