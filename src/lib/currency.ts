/** Formats a Rand amount the way this app's reward copy always shows it:
 * "R2.00", "R10.00" -- no thousands separator or space, matching the exact
 * style used throughout the reward feature's design examples. This is a
 * display-only helper; every actual amount always comes from the server
 * (submit_attempt RPC / reward_transactions), never computed client-side. */
export function formatRands(amount: number): string {
  return `R${amount.toFixed(2)}`
}
