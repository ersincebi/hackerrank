function getLetter(s) {
	let letter;
	// Write your code here
	const firstLetter = s[0]

	switch (true) {
		case 'aeiou'.includes(firstLetter):
			letter = 'A';
			break;
		case 'bcdfg'.includes(firstLetter):
			letter = 'B';
			break;
		case 'hjklm'.includes(firstLetter):
			letter = 'C';
			break;
		case 'npqrstvwxyz'.includes(firstLetter):
			letter = 'D';
		break;
	}
	return letter;
}


function main() {
	const s = 'adfgt' // readLine();
	
	console.log(getLetter(s));
}

main()