package db

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

// type news struct {
// 	title  string
// 	link   string
// 	source string
// 	time   string
// }

func Db_query_rst(condition string) []map[string]string {
	// Open database connection
	db, err := sql.Open("mysql", "test:123456@/crawler")
	if err != nil {
		panic(err.Error()) // Just for example purpose. You should use proper error handling instead of panic
	}
	defer db.Close()

	// Execute the query
	rows, err := db.Query("SELECT * FROM " + condition)
	if err != nil {
		panic(err.Error()) // proper error handling instead of panic in your app
	}

	// Get column names
	columns, err := rows.Columns()
	if err != nil {
		panic(err.Error()) // proper error handling instead of panic in your app
	}

	// Make a slice for the values
	values := make([]sql.RawBytes, len(columns))

	// rows.Scan wants '[]interface{}' as an argument, so we must copy the
	// references into such a slice
	// See http://code.google.com/p/go-wiki/wiki/InterfaceSlice for details
	scanArgs := make([]interface{}, len(values))
	for i := range values {
		scanArgs[i] = &values[i]
	}

	var rst []map[string]string
	// Fetch rows
	for rows.Next() {
		// get RawBytes from data
		err = rows.Scan(scanArgs...)
		if err != nil {
			panic(err.Error()) // proper error handling instead of panic in your app
		}

		// Now do something with the data.
		// Here we just print each column as a string.
		var value string
		record := make(map[string]string)

		for i, col := range values {
			// Here we can check if the value is nil (NULL value)
			if col == nil {
				value = "NULL"
			} else {
				value = string(col)
			}
			record[string(columns[i])] = value
			fmt.Println(columns[i], ": ", value)
		}
		rst = append(rst, record)
		// fmt.Println("-----------------------------------")

	}
	if err = rows.Err(); err != nil {
		panic(err.Error()) // proper error handling instead of panic in your app
	}
	return rst
}
