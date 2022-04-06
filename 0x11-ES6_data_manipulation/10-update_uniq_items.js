export default function updateUniqueItems(groceriesList) {
  if (!(groceriesList instanceof Map)) {
    throw Error('Cannot process');
  }
  groceriesList.forEach((key, value) => {
    if (key === 1) {
      groceriesList.set(value, 100);
    }
  });
  return groceriesList;
}
