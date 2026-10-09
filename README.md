# Spotify vs. Apple Music: a product and pricing teardown (India focus)

*By Pratiksh Pandita · Last updated: October 2026 · Built from public sources only*

## The question

Since July 2026, Spotify and Apple Music charge exactly the same ₹139 a month for one person in India, and the same ₹69 for students. If price no longer separates them, what does, and what should Spotify do next?

I focus on Spotify for two reasons. It has more at stake: it cut its price by ₹60 in May 2026, yet today it is only level with Apple. And it publishes its numbers, so each recommendation can be tied to a metric it already reports.

## Key facts (October 2026)

- **Same price for one person.** Spotify cut Premium Standard from ₹199 to ₹139 in May 2026. Apple raised Apple Music Individual from ₹119 to ₹139 in July 2026.
- **Different group plans.** Spotify Premium Platinum costs ₹299 for up to 3 people at the same address. Apple Music Family costs ₹229 for up to 6 people. Spotify closed its Duo and Family plans to new Indian users in November 2025.
- **Different audio quality at the same price.** Apple Music includes lossless and Spatial Audio in every plan. Spotify India includes lossless only in Platinum.
- **Different entry points.** Spotify has an ad-supported free tier. Apple Music offers only a one-month free trial.
- **One price edge left.** Spotify sells a 12-month prepaid Standard plan for ₹1,390 (about ₹116 a month). Apple's India page lists no annual option.
- **Scale.** Spotify had 777 million monthly active users and 300 million Premium subscribers in Q2 2026, with Premium ARPU of €4.89 a month. Apple does not disclose Apple Music figures.

![India one-person price over time](visuals/india_one_person_price.png)

![India plans compared](visuals/india_plans_compared.png)

## Recommendations for Spotify in India

### How I weighed the options

I listed five moves and judged each on three things: how strongly the facts in this repo support it, how much it could move paying subscribers, and what it could cost Spotify. The ratings are my judgment, not measured values.

| Option | Evidence in this repo | Likely impact | Cost or risk | Verdict |
|---|---|---|---|---|
| A. Reopen a household plan | Strong: ₹100 a person on Platinum vs. ₹38 on Apple Family, and no 6-person plan for new users | High | Medium: some current subscribers may move to a cheaper shared plan | **Do, as a test** |
| B. Push the prepaid annual plan to the most active free users | Strong: neither the free tier nor a ₹116-a-month annual price has an Apple equivalent in India | Medium | Low: both already exist | **Do** |
| C. Give Standard users a short Platinum trial | Medium: Apple includes lossless at ₹139; Spotify charges ₹299 for lossless | Medium | Low | **Do** |
| D. Add lossless to the ₹139 Standard plan | Medium | Medium | High: removes the main reason to buy Platinum | Don't |
| E. Cut Standard below ₹139 | Weak: Apple was the cheaper option until July 2026, and nothing here shows price decides who wins | Unclear | High: lowers Premium ARPU (€4.89 a month in Q2 2026) and invites a price war | Don't |

### 1. Test a household plan for up to 6 people
- **What:** Reopen a family-style plan for new users in India, priced close to Apple's ₹229, and test it in a few cities before a full launch.
- **Why:** For households, Spotify is the expensive option. Its largest plan for new users costs ₹100 a person for up to 3 people; Apple Family costs ₹38 a person for up to 6. Since November 2025, a new Indian household has had no 6-person option on Spotify at all.
- **Measure:** New paying households per week in test cities vs. similar cities without the plan. Guardrail: how many buyers were already paying for Standard individually, since several Standard payers merging into one shared plan lowers revenue.

### 2. Offer the prepaid annual plan to the most active free users
- **What:** Show the ₹1,390 prepaid annual plan to heavy free listeners at the moments the free tier limits them, instead of only the monthly price.
- **Why:** These are Spotify's two remaining price advantages. The free tier builds a listening habit that Apple's one-month trial can't, and the annual plan works out to about ₹116 a month, below Apple's ₹139.
- **Measure:** Free-to-paid conversion among users shown the offer, compared with a holdout group. Also track how many annual buyers renew after 12 months.

### 3. Let Standard users try Platinum for 14 days
- **What:** Keep lossless in Platinum, but give Standard subscribers a short Platinum trial so they hear the difference and try the AI DJ and other Platinum tools.
- **Why:** At ₹139, an Apple user gets lossless and Spotify's Standard user doesn't. Matching that would empty Platinum (option D), so let users experience it and choose to upgrade instead.
- **Measure:** Platinum upgrade rate after the trial. Guardrail: Standard cancellations among trial users once the trial ends.

### What would change my mind
- If the household test shows most buyers were Standard payers merging their accounts, recommendation 1 loses money and should stop.
- I don't know why Spotify closed Family and Duo to new users in 2025. If it was to limit account sharing, a household plan needs the same address check that Platinum already uses.

## What's inside

| File | What it covers |
|---|---|
| [reports/business_model.md](reports/business_model.md) | Revenue streams, ARPU, retention, pricing in India and the US |
| [reports/feature_analysis.md](reports/feature_analysis.md) | Podcasts, audio quality, discovery, ecosystem, pace of new features |
| [reports/UX_comparison.md](reports/UX_comparison.md) | Navigation, personalization and visual design |
| [data/pricing.csv](data/pricing.csv) | Current plans and prices in India and the US, with a source link for every row |
| [data/india_price_changes.csv](data/india_price_changes.csv) | Every Indian price change since November 2025, with sources |
| [scripts/make_charts.py](scripts/make_charts.py) | Rebuilds both charts from the CSV files (`python scripts/make_charts.py`) |

## Method

- Prices come from Spotify's and Apple's own plan pages, checked on 9 October 2026. Each row in `data/pricing.csv` links to its source.
- The dates of past price changes come from news reports, linked in `data/india_price_changes.csv`.
- Spotify's user and revenue figures come from its Q2 2026 results.
- Feature and user-experience notes compare the two apps as offered in India.

## Limitations

- Apple does not publish Apple Music subscriber, revenue or ARPU figures, so business comparisons are one-sided.
- Prices are list prices for new subscribers. Existing subscribers, promotions and bundles (such as Apple One) can pay less.
- Feature notes are qualitative and can change with any app update.
