---
title: "ModelDoc2::EditDimensionProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__EditDimensionProperties.htm"
---

# ModelDoc2::EditDimensionProperties

This
method is now obsolete and has been superseded by[ModelDoc2::EditDimensionProperties2](ModelDoc2__EditDimensionProperties2.htm).

Description

This method edits the currently selected dimension's
properties.

Syntax (OLE Automation)

retval = ModelDoc2.EditDimensionProperties (tolType, tolMax, tolMin, tolMaxFit, tolMinFit, useDocPrec,
precision, arrowsIn, useDocArrows, arrow1, arrow2)

(Table)=========================================================

| Input: | (long) tolType | Type of tolerance as defined in swTolType_e |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum value for the tolerance |
| Input: | (double) tolMin | Minimum value for the tolerance |
| Input: | (BSTR) tolMaxFit | Text for
the maximum FIT value when using a fit tolerance type |
| Input: | (BSTR) tolMinFit | Text for the maximum FIT value when using a fit
tolerance type |
| Input: | (BOOL) useDocPrec | TRUE to use the documents precision value FALSE
otherwise |
| Input: | (long) precision | Precision value to use for this dimension |
| Input: | (long) arrowsIn | Value for the arrow direction as defined in swDimensionArrowsSide_e |
| Input: | (BOOL) useDocArrows | TRUE to use the documents arrow types, FALSE
otherwise |
| Input: | (long) arrow1 | Type of arrow to use on the first arrow of this
dimension as defined in swArrowStyle_e |
| Input: | (long) arrow2 | Type of arrow to use on the second arrow of this
dimension as defined in swArrowStyle_e |
| Return: | (BOOL) retval | TRUE if the dimension is modified, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->EditDimensionProperties (
tolType, tolMax, tolMin, tolMaxFit, tolMinFit, useDocPrec, precision,
arrowsIn, useDocArrows, arrow1, arrow2, &retval )

(Table)=========================================================

| Input: | (long) tolType | Type of tolerance as defined in swTolType_e |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum value for the tolerance |
| Input: | (double) tolMin | Minimum value for the tolerance |
| Input: | (BSTR) tolMaxFit | Text for the maximum FIT value when using a fit
tolerance type |
| Input: | (BSTR) tolMinFit | Text string for the maximum FIT value when using
a fit tolerance type |
| Input: | (VARIANT_BOOL) useDocPrec | TRUE to use the documents precision value, FALSE
otherwise |
| Input: | (long) precision | Precision value to use for this dimension |
| Input: | (long) arrowsIn | Value for the arrow direction as defined in swDimensionArrowsSide_e |
| Input: | (VARIANT_BOOL) useDocArrows | TRUE to use the documents arrow types, FALSE
otherwise |
| Input: | (long) arrow1 | Type of arrow to use on the first arrow of this
dimension as defined in swArrowStyle_e |
| Input: | (long) arrow2 | Type of arrow to use on the second arrow of this
dimension as defined in swArrowStyle_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__EditDimensionProperties.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__EditDimensionProperties.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
