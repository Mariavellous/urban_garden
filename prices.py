import stripe
stripe.api_key = "sk_test_51LnxGxLeJ6gUVN1HtAzkLzp60PvEXngfpuB65r4t8Sue90iidTFvmkRfajTxiJB2YFPlNquktcSBr0ue5LiC4wzX00lf1EVPJN"

stripe.Price.create(
    currency="usd",
    product="kalamansi",
    unit_amount=150

)

stripe.Price.create(
    currency="usd",
    product="kamatis",
    unit_amount=199
)

stripe.Price.create(
    currency="usd",
    product="kalabasa",
    unit_amount=85
)

stripe.Price.create(
    currency="usd",
    product="talong",
    unit_amount=350
)

stripe.Price.create(
    currency="usd",
    product="sitaw",
    unit_amount=149
)

stripe.Price.create(
    currency="usd",
    product="okra",
    unit_amount=336
)

stripe.Price.create(
    currency="usd",
    product="silingmaanghang",
    unit_amount=400
)

stripe.Price.create(
    currency="usd",
    product="upo",
    unit_amount=106
)

