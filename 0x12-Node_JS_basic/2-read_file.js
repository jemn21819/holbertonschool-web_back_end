const fs = require('fs');

module.exports = function countStudents(pathFile) {
  const cs = [];
  const swe = [];
  try {
    const data = fs.readFileSync(pathFile, 'UTF-8');
    const lines = data.split(/\r?\n/);
    lines.forEach((line) => {
      if (line.includes('CS')) {
        cs.push(line.split(',')[0]);
      } else if (line.includes('SWE')) {
        swe.push(line.split(',')[0]);
      }
    });
    console.log(`Number of students: ${cs.length + swe.length}`);
    console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
    console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};
