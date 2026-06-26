---
title: "ModelDoc2::InsertCutBlend"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertCutBlend.htm"
---

# ModelDoc2::InsertCutBlend

This method is obsolete and has been superseded
by[ModelDoc2::InsertCutBlend2](ModelDoc2__InsertCutBlend2.htm).

Description

This method inserts a lofted cut based on the
selected profiles and guide curves. Selection of guide curves is optional;
however, selection of the profiles must be in an order consistent with
the desired direction of the loft.

Syntax (OLE Automation)

ModelDoc2.InsertCutBlend ( closed )

(Table)=========================================================

| Input: | (VARIANT_BOOL) closed | TRUE for a closed loft, FALSE for an open loft;
if TRUE and if you have selected less than three profiles, any selected
guide curves must be closed curves |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->InsertCutBlend ( closed )

Parameters Table Start

(Table)=========================================================

| Input: | (VARIANT_BOOL) closed | TRUE for a closed loft, FALSE for an open loft;
if TRUE and if you have selected less than three profiles, any selected
guide curves must be closed curves |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use of guide curves is recommended especially when
selection of profiles is done in the FeatureManager design tree.

You can use any number of profiles; however, if you have selected less
that three profiles, then any selected guide curves must be closed curves.

Use ModelDocExtension::SelectByIDto select
the profiles and guide curves. The markfor:

- profile selections should be a 1.
- any guide curve selection, if provided, should
  be a 2.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__InsertCutBlend.htm" >
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
<param name="Items" value="ModelDoc2 Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__InsertCutBlend.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
