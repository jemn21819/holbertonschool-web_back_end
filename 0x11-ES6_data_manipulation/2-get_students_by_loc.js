export default function getStudentsByLocation(arrays, city) {
  return arrays.filter((array) => array.location === city);
}
