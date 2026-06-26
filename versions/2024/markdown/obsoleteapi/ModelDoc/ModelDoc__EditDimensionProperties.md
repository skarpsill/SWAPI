---
title: "ModelDoc::EditDimensionProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditDimensionProperties.htm"
---

# ModelDoc::EditDimensionProperties

This
method is now obsolete and has been superseded by[ModelDoc::EditDimensionProperties2](ModelDoc__EditDimensionProperties2.htm).

Description

This method edits the currently selected dimension's
properties.

Syntax (OLE Automation)

retval = ModelDoc.EditDimensionProperties (tolType, tolMax, tolMin, tolMaxFit, tolMinFit, useDocPrec,
precision, arrowsIn, useDocArrows, arrow1, arrow2)

(Table)=========================================================

| Input: | (long) tolType | Type of tolerance you want to use as defined in swTolType_e |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum value for the tolerance |
| Input: | (double) tolMin | Minimum value for the tolerance |
| Input: | (BSTR) tolMaxFit | Text string for the maximum FIT value when using
a fit tolerance type |
| Input: | (BSTR) tolMinFit | Text string for the maximum FIT value when using
a fit tolerance type |
| Input: | (BOOL) useDocPrec | TRUE to use the documents precision value, FALSE
otherwise |
| Input: | (long) precision | Precision value to use for this dimension |
| Input: | (long) arrowsIn | Value for the arrow direction as defined in swDimensionArrowsSide_e |
| Input: | (BOOL) useDocArrows | TRUE to use the documents arrow types, FALSE
otherwise |
| Input: | (long) arrow1 | Type of arrow to use on the first arrow of this
dimension as defined in swArrowStyle_e |
| Input: | (long) arrow2 | Type of arrow to use on the second arrow of this
dimension as defined in swArrowStyle_e |
| Return: | (BOOL) retval | TRUE if the dimension was successfully edited,
FALSE otherwise |

Syntax (COM)

status = ModelDoc->EditDimensionProperties ( tolType,
tolMax, tolMin, tolMaxFit, tolMinFit, useDocPrec, precision, arrowsIn,
useDocArrows, arrow1, arrow2, &retval )

(Table)=========================================================

| Input: | (long) tolType | Type of tolerance you want to use as defined in swTolType_e |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum value for the tolerance |
| Input: | (double) tolMin | Minimum value for the tolerance |
| Input: | (BSTR) tolMaxFit | Maximum FIT value when using a fit tolerance
type |
| Input: | (BSTR) tolMinFit | Maximum FIT value when using a fit tolerance
type |
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
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__EditDimensionProperties.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
