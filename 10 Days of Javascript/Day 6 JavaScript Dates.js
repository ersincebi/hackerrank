function getDayName(dateString) {
	let dayName = [
		'Sunday',
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday'
	];
	const date = new Date(dateString)
	const dayNum = date.getDay();
	// Sunday - Saturday : 0 - 6

	return dayName[dayNum]
}


function main() {
	const d = [
		'10/11/2009',
		'11/10/2010'
	]
	
	for (let i = 0; i < d.length; i++) {
		const date = d[i]
		
		console.log(getDayName(date));
	}
}

main()