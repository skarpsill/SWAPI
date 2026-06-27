---
title: "Loop::IsOuter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__IsOuter.htm"
---

# Loop::IsOuter

This method is obsolete
and has been superseded by[Loop2::IsOuter](sldworksAPI.chm::/Loop2/Loop2__IsOuter.htm).

Description

This method tells you if the loop is the outermost loop on the face.

Syntax (OLE Automation)

retval = Loop.IsOuter ()

(Table)=========================================================

| Return: | (BOOL) retval | TRUE if the loop is the outermost loop, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = Loop->IsOuter ( &retval
)

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if the loop is the outermost loop, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Some situations exist where no clear outer loop is defined. For example,
the cylindrical face of an extruded circle has two loops that could be
considered outer loops.

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
<param name="Items" value="Loop_Object$$**$$ZGetInfoLoop$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Loop\Loop__IsOuter.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
