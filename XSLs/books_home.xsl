<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
    <head>
    <title>Books</title>
    </head>
    <body>
    <h1 align = "center">Books</h1>
    <ol>
    <xsl:for-each select = "books/item">
    <xsl:sort select="title"/>
    <xsl:variable name="titlevar" select = "title"/>
    <li><a href="{concat($titlevar,'.html')}"><xsl:value-of select="title"/></a></li>
    </xsl:for-each>
    </ol>
    </body>
    </html>
   </xsl:template>
</xsl:stylesheet>