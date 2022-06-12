const fs = require('fs');

module.exports = function countStudents(path) {
  const cs = [];
  const swe = [];
  const response = [];

  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (e, data) => {
      if (e) {
        reject(Error('Cannot load the database'));
        return;
      }
      data.split(/\r?\n/).forEach((l) => {
        if (l.includes('CS')) {
          cs.push(l.split(',')[0]);
        } else if (l.includes('SWE')) {
          swe.push(l.split(',')[0]);
        }
      });
      console.log(`Number of students: ${cs.length + swe.length}`);
      console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
      console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
      response.push(`Number of students: ${cs.length + swe.length}`);
      response.push(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
      response.push(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
      resolve({
        response,
      });
    });
  });
};
