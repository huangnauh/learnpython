<?xml version="1.0" encoding="ISO-8859-1"?>
<!-- Edited with XML Spy v2007 (http://www.altova.com) -->
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="catalog">
  <html>
  <body>

    <xsl:for-each select="cd">
        <tr>
            <td><xsl:value-of select="@id"/></td>
        </tr>
    </xsl:for-each>
	<!--<xsl:apply-templates></xsl:apply-templates>-->
  </body>
  </html>
</xsl:template>


<!--<xsl:template match="cd">
    <p>
        <xsl:apply-templates select="title"/>
        <xsl:apply-templates select="artist"/>
    </p>
</xsl:template>

<xsl:template match="title">
    Title: <span style="color:#ff0000">
    <xsl:value-of select="."></xsl:value-of>
    </span>
</xsl:template>
<xsl:template match="artist">
    Title: <span style="color:#00ff00">
    <xsl:value-of select="."></xsl:value-of>
    </span>
</xsl:template>-->
</xsl:stylesheet>