<div class="entity" data-entity-id="fund">
  <table style="border-style:solid;border-width:2px;border-color:rgb(55, 95, 146);margin:1px;">
    <tr>
      <td colspan="2" class="tempo-text-color--white" style="background-color:rgb(55, 95, 146);padding:10px 10px 0 10px;font-size:18pt;font-family: 'Century Gothic', 'Trebuchet MS';border:none">
        <b>${entity['fund']['Funds']}</b>
      </td>
    </tr>
    <tr>
      <td colspan="2" style="background-color:rgb(55, 95, 146);padding:10px;font-family: 'Century Gothic', 'Trebuchet MS';border:none" class="tempo-text-color--white">
        <span style="padding-right:30px"><b>NAV</b> ${entity['fund']['Latest NAV']}</span>
        <span style="padding-right:30px"><b>CCY</b> ${entity['fund']['Base Ccy']}</span>
        <span style="padding-right:30px"><b>ISIN</b> ${entity['fund']['ISIN (base ccy)']}</span>
        <span style="padding-right:30px"><b>Risk Rating</b> ${entity['fund']['Risk Rating']}</span>
        <span><b>AR*</b> ${entity['fund']['AR*']}</span>
      </td>
    </tr>
    <tr>
      <td style="border:none;width:50%;padding-bottom:15px;">
        <table style="margin:0">
          <tr>
            <td colspan="2" style="padding:5px 10px 20px 10px;text-align:center;font-size:14pt;border:none">
              <div style="border-bottom:rgb(55, 95, 146) 3px solid;padding:5px;font-family: 'Century Gothic', 'Trebuchet MS';">SUITABILITY</div>
            </td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>Investment Objective</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['Investment Objective']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>Investment Tenor</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['Investment Tenor']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>Investment Time Horizon</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['Investment Time Horizon']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>Loss Absorption Product</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['Loss Absorption Product']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>Complex Product</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['Complex Product']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>High Yield Bond Fund</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['Is this a High Yield Bond Fund (Yes/No)']}</td>
          </tr>
        </table>
      </td>

      <td style="border:none;width:50%;padding-bottom:15px;">
        <table style="margin:0">
          <tr>
            <td colspan="2" style="padding:5px 10px 20px 10px;text-align:center;font-size:14pt;border:none">
              <div style="border-bottom:rgb(55, 95, 146) 3px solid;padding:5px;font-family: 'Century Gothic', 'Trebuchet MS';">PERFORMANCE</div>
            </td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>Last Bloomberg Update</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['Last Bloomberg Update']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>1 Month Return (%)</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['1 Mth Return (%)']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>3 Month Return (%)</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['3 Mths Return (%)']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>YTD Month Return (%)</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['YTD Return (%)']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>1 Year Return (%)</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['1 Yr Return (%)']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>>3 Year Annual Return (%)</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['3 Yr Ann Return (%)']}</td>
          </tr>
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>3 Year Annual Std Dev (%)</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['3 Yr Ann Std Dev (%)']}</td>
          </tr>          
          <tr>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';"><b>Dealing Frequency</b></td>
            <td style="border:none;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['Dealing Frequency (Subscription) Refer to Funds Identifier tab for Notice Period']}</td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td colspan="2" style="text-align:right;border-top:#ccc 1px solid;padding:15px;font-weight:bold;font-family: 'Century Gothic', 'Trebuchet MS';">
        <#if entity['fund']['Factsheet / Offering Material (via Fundinfo)']!="N/A">
        <span style="padding-right:25px">
          <a href="${entity['fund']['Factsheet / Offering Material (via Fundinfo)']}">Fund Documents</a>
        </span>
        </#if>
      </td>
    </tr>
  </table>
</div>
<span style="font-size:9pt;font-family: 'Century Gothic', 'Trebuchet MS';">Please note that this information is strictly for internal use only and must not be circulated</span>
<#if entity['fund']['Extra Remarks']!="N/A">
<br/><span style="font-size:9pt;font-family: 'Century Gothic', 'Trebuchet MS';">${entity['fund']['Extra Remarks']}</span>  
 </#if>
