<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <title>FanFiction</title>
        <link rel="stylesheet" href="./main.css"/>
        <link rel="stylesheet" href="./bootstrap.min.css"/>
      </head>
      <body>
          <div class="container-fluid">
            <div class="row">
              <h3>FanFictions</h3>
              <xsl:apply-templates/>
            </div>
          </div>
          <script>
            function showStory(event) {
              var parent = event.target.offsetParent;
              parent.nextSibling.classList.remove("hidden");
              parent.firstChild.remove();
              var grandParent = parent.offsetParent;
              grandParent.classList.remove("titlesDiv");
              grandParent.classList.add("activeStory");
            }
          </script>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="item">
    <div class="col-xl-4 col-lg-4 col-md-4 col-sm-4 col-xs-4 titlesDiv contentDiv">
      <xsl:apply-templates select="bookTitle"/>
      <xsl:apply-templates select="fictions"/>
    </div>
  </xsl:template>

  <xsl:template match="bookTitle">
    <br/>
    <b><xsl:value-of select="." /></b> - 
  </xsl:template>

  <xsl:template match="fictions">
    <xsl:value-of select="./title"/>
    <br/>
    <i>by <xsl:value-of select="./author"/></i>
    <br/><br/>
    <span class="otherInfo">
      <i><xsl:value-of select="./otherInfo"/></i>
    </span>
    <br/><br/>
    <span class="storySpan">
      <b onclick="showStory(event)"><i>CLICK HERE TO READ STORY</i></b> 
      <p class="hidden storyPara">
        <xsl:value-of select="./story"/>
      </p>
    </span>
  </xsl:template>

  <xsl:template match="text()"/>
</xsl:stylesheet>
