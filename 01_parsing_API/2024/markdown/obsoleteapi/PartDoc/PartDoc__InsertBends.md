---
title: "PartDoc::InsertBends"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__InsertBends.htm"
---

# PartDoc::InsertBends

This method is obsolete and has been superseded
by[PartDoc::InsertBends2](sldworksAPI.chm::/PartDoc/PartDoc__InsertBends2.htm).

Description

This method creates bends in a thin-feature part.

Syntax (OLE Automation)

retval = PartDoc.InsertBends ( radius, useBendTable,
useKfactor, useBendAllowance, useAutoRelief, offsetRatio )

(Table)=========================================================

| Input: | (double)radius | Radius of the bends |
| --- | --- | --- |
| Input: | (BSTR)useBendTable | Bend table name (.btl file) |
| Input: | (double) useKfactor | K-Factor ratio or -1 if not used |
| Input: | (double) useBendAllowance | Bend allowance value or -1 if not used |
| Input: | (VARIANT_BOOL) useAutoRelief | TRUE if auto-relief cuts are to be added |
| Input: | (double) offsetRatio | Distance relief cut extends beyond bend |
| Input: | (VARIANT_BOOL) retval | TRUE for success, FALSE for failure |

Syntax (COM)

status = PartDoc->InsertBends
( radius, useBendTable, useKfactor, useBendAllowance, useAutoRelief, offsetRatio,
retval )

(Table)=========================================================

| Input: | (double)radius | Radius of the bends |
| --- | --- | --- |
| Input: | (BSTR)useBendTable | Bend table name (.btl file) |
| Input: | (double) useKfactor | K-Factor ratio or -1 if not used |
| Input: | (double) useBendAllowance | Bend Allowance value or -1 if not used |
| Input: | (VARIANT_BOOL) useAutoRelief | TRUE if auto-relief cuts are to be added |
| Input: | (double) offsetRatio | Distance relief cut extends beyond bend |
| Input: | (VARIANT_BOOL) retval | TRUE for success, FALSE for failure |
| Return: | (HRESULT )status | S_OK if successful |

Remarks

For more information about these arguments, see SolidWorks Help.

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
<param name="Items" value="ModelDoc_Object$$**$$ZInsertFeature$$**$$ZModifyBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\PartDoc\PartDoc__InsertBends.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
