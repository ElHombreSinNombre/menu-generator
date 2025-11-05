CREATE DATABASE IF NOT EXISTS menu;

USE menu;

CREATE TABLE foods (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ean VARCHAR(13) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    carbohydrates_g DECIMAL(10,2) NOT NULL,
    fats_g DECIMAL(10,2) NOT NULL,
    proteins_g DECIMAL(10,2) NOT NULL
);

INSERT INTO foods (ean, name, carbohydrates_g, fats_g, proteins_g) VALUES
('8410000000001', 'Whole Wheat Bread', 45.00, 3.50, 10.00),
('7501000000005', 'Chicken Breast (Grilled)', 0.00, 4.00, 31.00),
('5449000000000', 'Brown Rice (Cooked)', 39.00, 1.00, 4.00),
('0003400000000', 'Avocado (Medium)', 8.50, 29.00, 4.00),
('9780100000003', 'Salmon Fillet (Baked)', 0.00, 13.00, 41.00),
('4002100000000', 'Spinach Salad', 5.00, 2.00, 3.00),
('6009800000000', 'Protein Bar (Chocolate)', 25.00, 8.00, 20.00),
('8008000000000', 'Plain Yogurt (Greek)', 6.00, 5.00, 17.00);
