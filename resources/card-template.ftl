<div class="entity" data-entity-id="fund">
  <h2>MI Flashcard</h2>
  <br/>
  <table style="border-style: solid;border-width: 2px;border-color:rgb(0, 88, 140);margin:0;">
    
    <thead>
      <tr>
        <td colspan ="2" style="padding: 0;background-color:rgb(0, 88, 140);text-align: center;"><span class="tempo-text-color--white"><span style="font-size: 18pt;"><b>
          ${entity['fund']['Funds']}
          </b></span></span></td>
      </tr>
    </thead>

    <tbody style="padding:0;">
      <tr>
        <td style="padding:0px;">
          
          <table style="margin:0;">
            
           <thead>
                <tr>
                  <td colspan ="2" style="padding: 0;text-align: center;"><span style="font-size: 14pt;"><b>
                    SUITABILITY
                  </b></span></td>
                </tr>
              </thead>
            
            <tbody>
              <tr>
                <td>NAV</td>
                <td>$100</td>
              </tr>
              <tr>
                <td>Base Currency</td>
                <td>${entity['fund']['Base Ccy']}</td>
              </tr>
              <tr>
                <td>ISIN (Base Currency)</td>
                <td>${entity['fund']['ISIN (base ccy)']}</td>
              </tr>
              <tr>
                <td>Investment Objective</td>
                <td>${entity['fund']['Investment Objective']}</td>
              </tr>
              <tr>
                <td>Investment Tenor</td>
                <td>${entity['fund']['Investment Tenor']}</td>
              </tr>
              <tr>
                <td>Investment Time Horizon</td>
                <td>>${entity['fund']['Investment Time Horizon']}</td>
              </tr>
              <tr>
                <td>Loss Absorption Product</td>
                <td>${entity['fund']['Loss Absorption Product']}</td>
              </tr>
              <tr>
                <td>Complex Product</td>
                <td>${entity['fund']['Complex Product']}</td>
              </tr>
              <tr>
                <td>Fund Factsheet</td>
                <td><a href="${entity['fund']['Factsheet / Offering Material (via Fundinfo)']}">Link</a></td>
              </tr>
              <tr>
                <td>More Information</td>
                <td><a href="${entity['fund']['Fund Specific Materials (via Intranet)']}">Link</a></td>
              </tr>
            </tbody>
          </table>
        </td>

        <td style="padding:0px;">
          
          <table style="margin:0;">
            
			<thead>
                <tr>
                  <td colspan ="2" style="padding: 0;text-align: center;"><span style="font-size: 14pt;"><b>
                    PERFORMANCE
                  </b></span></td>
                </tr>
            </thead>
            
            <tbody>
              <tr>
                <td>Last Bloomberg Update</td>
                <td>${entity['fund']['Last Bloomberg Update']}</td>
              </tr>
              <tr>
                <td>1 Month Return (%)</td>
                <td>${entity['fund']['1 Mth Return (%)']}</td>
              </tr>
              <tr>
                <td>3 Month Return (%)</td>
                <td>${entity['fund']['3 Mths Return (%)']}</td>
              </tr>
              <tr>
                <td>YTD Month Return (%)</td>
                <td>${entity['fund']['YTD Return (%)']}</td>
              </tr>
              <tr>
                <td>1 Year Return (%)</td>
                <td>${entity['fund']['1 Yr Return (%)']}</td>
              </tr>
              <tr>
                <td>3 Year Return (%)</td>
                <td>${entity['fund']['3 Yr Ann Return (%)']}</td>
              </tr>
              <tr>
                <td><br/></td>
                <td></td>
              </tr>
              <tr>
                <td>Risk Rating</td>
                <td>${entity['fund']['Risk Rating']}</td>
              </tr>
              <tr>
                <td>AR*</td>
                <td>${entity['fund']['AR*']}</td>
              </tr>
              <tr>
                <td>Dealing Frequency</td>
                <td>${entity['fund']['Dealing Frequency (Subscription) Refer to Funds Identifier tab for Notice Period']}</td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>

    <tfoot>
      <tr>
        <td colspan ="2" style="border-style: solid;border-width: 2px;border-color:rgb(0, 88, 140);padding: 0;"><span style="font-size: 9pt;"><br/>
          Please note that this information is strictly for internal use only and must not be circulated
        </span></td>
      </tr>
    </tfoot>
  </table>
</div>