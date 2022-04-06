export default function cleanSet(set, startString) {
  const lst = [];
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }
  for (const item of set) {
    if (typeof item === 'string' && item.startsWith(startString)) {
      lst.push(item.slice(startString.length));
    }
  }
  return lst.join('-');
}
