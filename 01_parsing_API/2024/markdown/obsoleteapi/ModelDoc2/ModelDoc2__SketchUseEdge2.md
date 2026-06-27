---
title: "ModelDoc2::SketchUseEdge2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchUseEdge2.htm"
---

# ModelDoc2::SketchUseEdge2

This method is obsolete and has been superseded
by[SketchManager::SketchUseEdge](sldworksAPI.chm::/SketchManager/SketchManager__SketchUseEdge.htm).

Description

This method uses the selected edges to generate geometry in the active
sketch.

Syntax (OLE Automation)

retval = ModelDoc2.SketchUseEdge2 ( chain )

(Table)=========================================================

| Input: | (BOOL) chain | TRUE if you want entire chain of entities offset,
FALSE if you want only selected sketch entities offset (see Remarks ) |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the offset is successful, FALSE if not |

Syntax (COM)

status = ModelDoc2->SketchUseEdge2 ( chain, &retval
)

(Table)=========================================================

| Input: | (VARIANT_BOOL) chain | TRUE if you want entire chain of entities offset,
FALSE if you want only selected sketch entities offset (see Remarks ) |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the offset is successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Specifying TRUE to the chain argument offsets the
selected entity and any other entities that belong to the same contour
or chain (contiguous, geometric entities like edges).

See ModelDoc2::SketchOffsetEntities2 method for
similar functionality.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__SketchUseEdge2.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__SketchUseEdge2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
