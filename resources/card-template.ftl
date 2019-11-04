<div class="entity" data-entity-id="fund">
  <table style="border-style:solid;border-width:2px;border-color:rgb(55, 95, 146);margin:0;">
    <tr>
      <td colspan="2" class="tempo-text-color--white" style="background-color:rgb(55, 95, 146);padding:10px 10px 0 10px;font-size:18pt;border:none">
        <b>${entity['fund']['Funds']}</b>
      </td>
    </tr>
    <tr>
      <td colspan="2" style="background-color:rgb(55, 95, 146);padding:10px;border:none" class="tempo-text-color--white">
        <span style="padding-right:15px"><b>NAV</b> 100</span>
        <span style="padding-right:15px"><b>CCY</b> ${entity['fund']['Base Ccy']}</span>
        <span style="padding-right:15px"><b>ISIN</b> ${entity['fund']['ISIN (base ccy)']}</span>
        <span style="padding-right:15px"><b>Risk Rating</b> ${entity['fund']['Risk Rating']}</span>
        <span><b>AR*</b> ${entity['fund']['AR*']}</span>
      </td>
    </tr>
    <tr>
      <td style="border:none;width:50%;padding-bottom:15px;">
        <table style="margin:0">
          <tr>
            <td colspan="2" style="padding:5px 10px 20px 10px;text-align:center;font-size:14pt;border:none">
              <div style="border-bottom:rgb(55, 95, 146) 3px solid;padding:5px;">SUITABILITY</div>
            </td>
          </tr>
          <tr>
            <td style="border:none"><b>Investment Objective</b></td>
            <td style="border:none">${entity['fund']['Investment Objective']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>Investment Tenor</b></td>
            <td style="border:none">${entity['fund']['Investment Tenor']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>Investment Time Horizon</b></td>
            <td style="border:none">>${entity['fund']['Investment Time Horizon']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>Loss Absorption Product</b></td>
            <td style="border:none">${entity['fund']['Loss Absorption Product']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>Complex Product</b></td>
            <td style="border:none">${entity['fund']['Complex Product']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>High Yield Bond Fund</b></td>
            <td style="border:none">No</td>
          </tr>
        </table>
      </td>

      <td style="border:none;width:50%;padding-bottom:15px;">
        <table style="margin:0">
          <tr>
            <td colspan="2" style="padding:5px 10px 20px 10px;text-align:center;font-size:14pt;border:none">
              <div style="border-bottom:rgb(55, 95, 146) 3px solid;padding:5px;">PERFORMANCE</div>
            </td>
          </tr>
          <tr>
            <td style="border:none"><b>Last Bloomberg Update</b></td>
            <td style="border:none">${entity['fund']['Last Bloomberg Update']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>1 Month Return (%)</b></td>
            <td style="border:none">${entity['fund']['1 Mth Return (%)']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>3 Month Return (%)</b></td>
            <td style="border:none">${entity['fund']['3 Mths Return (%)']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>YTD Month Return (%)</b></td>
            <td style="border:none">${entity['fund']['YTD Return (%)']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>1 Year Return (%)</b></td>
            <td style="border:none">${entity['fund']['1 Yr Return (%)']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>3 Year Return (%)</b></td>
            <td style="border:none">${entity['fund']['3 Yr Ann Return (%)']}</td>
          </tr>
          <tr>
            <td style="border:none"><b>Dealing Frequency</b></td>
            <td style="border:none">${entity['fund']['Dealing Frequency (Subscription) Refer to Funds Identifier tab for Notice Period']}</td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td colspan="2" style="text-align:right;border-top:#ccc 1px solid;padding:15px;font-weight:bold;">
        <span style="padding-right:25px">
          <a href="${entity['fund']['Factsheet / Offering Material (via Fundinfo)']}">Fund Factsheet</a>
        </span>
        <span>
          <a href="${entity['fund']['Fund Specific Materials (via Intranet)']}">More Information</a>
        </span>
      </td>
    </tr>
  </table>
</div>
<span style="font-size:9pt">Please note that this information is strictly for internal use only and must not be circulated</span>