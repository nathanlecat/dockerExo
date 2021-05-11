const express = require('express');
const router = express.Router();
const productServices = require('../services/productService');

/* GET programming languages. */
router.get('/', async function(req, res, next) {
    try {
        res.json(await productServices.getMultiple(req.query.page));
    } catch (err) {
        console.error(`Error while getting programming languages `, err.message);
        next(err);
    }
});

module.exports = router;