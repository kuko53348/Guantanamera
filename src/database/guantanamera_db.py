guantanamera_database: dict = {
    "Consume": "A rich and flavorful Cuban consommé, slow-cooked with tender meats, fresh vegetables, and aromatic spices. A comforting bowl of warmth that delights the senses.",
    "Bannana Chips": "Crispy, golden banana chips lightly salted for the perfect balance of sweet and savory. A delicious and addictive snack that pairs well with any meal.",
    "Sauteed vegetables": "Fresh seasonal vegetables sautéed to perfection with garlic, olive oil, and a hint of citrus. A vibrant and healthy side dish bursting with flavor.",
    "Boiled food": "Tender meats and vegetables boiled with traditional Cuban spices, creating a hearty and wholesome dish that’s both simple and satisfying.",
    "Cold salad": "A refreshing mix of crisp greens, juicy tomatoes, cucumbers, and onions, tossed in a zesty lime vinaigrette. Perfect for a light and tangy bite.",
    "Garlic shrimp": "Succulent shrimp sautéed in a rich garlic butter sauce with a touch of white wine and fresh herbs. A seafood lover’s dream with bold, aromatic flavors.",
    "Perlan fish": "Fresh Perlan fish grilled to flaky perfection, seasoned with a blend of Cuban spices and served with a squeeze of lime. A taste of the ocean in every bite.",
    "Roasted chicken": "Juicy, golden-roasted chicken marinated in a blend of citrus and spices, with crispy skin and tender, flavorful meat. A classic dish done right.",
    "Chicken fajitas": "Sizzling strips of marinated chicken with bell peppers and onions, served with warm tortillas. A fiesta of flavors you can assemble to your liking.",
    "Pork fajitas": "Tender, spiced pork strips grilled with onions and peppers, served with soft tortillas and fresh toppings. A mouthwatering twist on a favorite.",
    "Pork steak": "A juicy, thick-cut pork steak grilled to perfection and glazed with a sweet and tangy mojo sauce. A hearty and satisfying centerpiece for any meal.",
    "Fish fillet": "Delicate white fish fillet lightly seasoned and pan-seared for a crispy exterior and moist, flaky interior. Simple, fresh, and utterly delicious.",
    "Grilled lobster small size": "A petite but luxurious lobster tail, grilled to tender perfection and basted with garlic butter. A taste of the sea in every succulent bite.",
    "Grilled lobster medium size": "A generous lobster tail, expertly grilled and drizzled with a rich, buttery sauce. Indulge in the sweet, delicate flavors of the ocean.",
    "Grilled lobster bigger size": "A majestic lobster tail, fire-grilled and served with a decadent garlic herb butter. The ultimate seafood indulgence for special occasions.",
    "All in one plate": "A vibrant Spanish-Cuban fusion paella loaded with lobster, mushrooms, calamari, and octopus, simmered in saffron-infused rice. A feast for the eyes and palate.",
    "Cuban paella": "A vibrant Spanish-Cuban fusion paella, marinated in Cuban spices and served with traditional sides. A classic combo with bold flavors.",
    "Cuban mixed": "A hearty plate of tender roasted chicken and succulent pork, marinated in Cuban spices and served with traditional sides. A classic combo with bold flavors.",
    "Sea and land Chiken": "The best of both worlds—flaky grilled fish and juicy roasted chicken, served with a medley of fresh sides. A harmonious blend of land and sea.",
    "Sea and land Pork": "Succulent pork and perfectly grilled fish come together in this flavorful duo, offering a taste of Cuba’s rich culinary traditions.",
    "Sea mixed": "A luxurious pairing of grilled lobster tail and fresh fish fillet, drizzled with citrusy mojo sauce. A seafood lover’s paradise on a plate.",
    "Guantanamera": "Our signature trio—grilled lobster, roasted chicken, and savory pork—served with classic Cuban sides. A feast fit for celebration.",
    "Special combo": "An extravagant combination of lobster, garlic shrimp, and tender pork, creating a symphony of flavors and textures. The pinnacle of Cuban indulgence.",
}


def get_database(index: str = ""):
    return guantanamera_database.get(index, "No exit")
