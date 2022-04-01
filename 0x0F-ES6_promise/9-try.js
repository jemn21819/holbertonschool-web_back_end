export default function guardrail(mathFunction) {
  const q = [];

  try {
    q.push(mathFunction());
  } catch (e) {
    q.push(e.toString());
  }
  q.push('Guardrail was processed');

  return q;
}
