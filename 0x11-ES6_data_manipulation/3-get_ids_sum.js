export default function getStudentIdsSum(students) {
  return students.reduce((i, value) => i + value.id, 0);
}
