odoo.define('point_of_sale_custom.NumpadWidgetExtension', function (require) {
    'use strict';

    const NumpadWidget = require('point_of_sale.NumpadWidget');
    const Registries = require('point_of_sale.Registries');

    const NumpadWidgetExtension = NumpadWidget =>
        class extends NumpadWidget {
            get hasManualDiscount() {
                return false;  
            }
            get hasPriceControlRights() {
                return false;  
            }
        };

    Registries.Component.extend(NumpadWidget, NumpadWidgetExtension);

    return NumpadWidget;
});
