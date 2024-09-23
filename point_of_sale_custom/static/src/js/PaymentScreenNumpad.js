odoo.define('point_of_sale.PaymentScreenNumpadExtension', function(require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const PaymentScreenNumpad = require('point_of_sale.PaymentScreenNumpad');

    PaymentScreenNumpad.template = 'PaymentScreenNumpad2';

    Registries.Component.add(PaymentScreenNumpad);

    return PaymentScreenNumpad;
});
