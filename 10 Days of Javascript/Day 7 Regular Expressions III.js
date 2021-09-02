function regexVar() {
	/*
	* Declare a RegExp object variable named 're'
	* It must match ALL occurrences of numbers in a string.
	*/
	let re = /\d+/g
	
	/*
	* Do not remove the return statement
	*/
	return re;
}


function main() {
	const re = regexVar();
	const s = "102, 1948948 and 1.3 and 4.5"// readLine();
	
	const r = s.match(re);
	
	for (const e of r) {
		console.log(e);
	}
}

main()