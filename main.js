const DSB = require('dsbapi');

const dsb = new DSB('243322', 'HammerHai21');

dsb.fetch()
	.then(data => {
		const timetables = DSB.findMethodInData('timetable', data);
    console.log(timetables)
		// Work with it
	})
	.catch(e => {
		// An error occurred :(
		console.log(e);
	});
