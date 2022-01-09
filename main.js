import DSB from 'dsbapi';

const dsb = new DSB('USERNAME', 'PASSWORD');

async function getMyShit() {
	const data = await dsb.fetch();
	const timetables = DSB.findMethodInData('timetable', data);
	const tiles = DSB.findMethodInData('tiles', data);

	// YEAH
}

getMyShit();
