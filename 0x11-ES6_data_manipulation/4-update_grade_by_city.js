export default function updateStudentGradeByCity(students, city, newGrades) {
  if (Array.isArray(students) === false) {
    return [];
  }
  return students.filter((student) => student.location === city).map((student) => {
    const [newGrade] = newGrades.filter((g) => g.studentId === student.id);
    return { ...student, grade: newGrade ? newGrade.grade : 'N/A' };
  });
}
