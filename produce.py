import stripe
stripe.api_key = "sk_test_51LnxGxLeJ6gUVN1HtAzkLzp60PvEXngfpuB65r4t8Sue90iidTFvmkRfajTxiJB2YFPlNquktcSBr0ue5LiC4wzX00lf1EVPJN"

stripe.Product.create(
    id="kalamansi",
    name="Calamansi (Philippine lime)",
    images=["https://www.justlovelylittlethings.com/wp-content/uploads/2019/05/315ED45D-CF90-4F3A-AA61-B263F027A41F.jpeg"],
    unit_label="lb",
)

stripe.Product.create(
    id="kamatis",
    name="Vine Tomatoes",
    images=["http://cdn.shopify.com/s/files/1/1249/8845/products/Vine_Ripened_Tomato_Fragrance_1024x.jpg?v=1501185763"],
    unit_label="lb",
)

stripe.Product.create(
    id="kalabasa",
    name="Calabaza",
    images=["https://i0.wp.com/www.donnaamisdavis.com/wp-content/uploads/2013/08/Kalabasa.jpg?resize=300%2C226&ssl=1"],
    unit_label="lb"
)

stripe.Product.create(
    id="talong",
    name="Japanese Eggplant",
    images=["https://4.bp.blogspot.com/-kEYJb3685D4/WBNx7iM8abI/AAAAAAAAExs/KFXi8LqvaoENtCL3OC3UQ8GolqOglzOVACLcB/s1600/Japanese%2Beggplant.JPG"],
    unit_label="lb"
)

stripe.Product.create(
    id="sitaw",
    name="String Beans",
    images=["https://panlasangpinoy.com/wp-content/uploads/2021/04/Can-You-Eat-Freeze-Fresh-String-Beans.jpg"],
    unit_label="lb"
)


stripe.Product.create(
    id="okra",
    name="Okra",
    images=["https://i1.wp.com/soupbelly.com/wp-content/uploads/2017/08/DSC_6401.jpg?fit=1024%2C690&ssl=1"],
    unit_label="lb"
)

stripe.Product.create(
    id="silingmaanghang",
    name="Thai Chili",
    images=["https://izzycooking.com/wp-content/uploads/2020/05/Thai-Peppers-1-683x1024.jpg"],
    unit_label="lb"
)

stripe.Product.create(
    id="upo",
    name="Upo (Bottle Gourd)",
    images=["https://1.bp.blogspot.com/-dq2iT9HZgrE/X8pE4RIOEmI/AAAAAAAAAEA/jXcayVe5RVca_s7ILnoXySNCSatiKHBcACLcBGAsYHQ/w1200-h630-p-k-no-nu/upo%2Btambuli.jpg"],
    unit_label="lb"
)