export const weakMap = new WeakMap();
export function queryAPI(apiEndpoint) {
  if (!weakMap.has(apiEndpoint)) {
    weakMap.set(apiEndpoint, 1);
  } else {
    weakMap.set(apiEndpoint, 1 + weakMap.get(apiEndpoint));
    if (weakMap.get(apiEndpoint) >= 5) {
      throw (Error('Endpoint load is high'));
    }
  }
}
