export default function getListStudentIds(arrays) {
  if (Array.isArray(arrays)) {
    return arrays.map((array) => array.id);
  }
  return [];
}
