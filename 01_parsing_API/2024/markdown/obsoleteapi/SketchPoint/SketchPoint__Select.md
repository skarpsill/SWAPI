---
title: "SketchPoint::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchPoint/SketchPoint__Select.htm"
---

# SketchPoint::Select

This
method is obsolete and has been superseded by SketchPoint::Select2 .

Description

This method selects the SketchPoint
object and appends it to the current set of selections or replaces the
entire selection list.

Syntax (OLE Automation)

retval = SketchPoint.Select (appendFlag)

(Table)=========================================================

| Input: | (BOOL) appendFlag | TRUE to append the item to the current selection
list, FALSE to replace the current selection list with this item |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successfully selected, FALSE if not |

Syntax (COM)

status = SketchPoint->Select ( appendFlag, &retval
)

(Table)=========================================================

| Input: | (VARIANT_BOOL) appendFlag | TRUE to append the item to the current selection
list, FALSE to replace the current selection list with this item |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method does not work well when a PropertyManager
page is open or a command is running. Use ModelDoc2::SelectByID instead
of using this method. ModelDoc2::SelectByID handles selection correctly
whether or not a command is running.

To select or deselect a sketch point, the owning
document of that SketchPoint object needs to be open and visible.

Sketch point selections are accessible through
the SelectionMgr of the owning document of the SketchPoint object, even
if the owning document is not active.

Selection or deselection does not work for a sketch
point in a document within a drawing. Selection or deselection of sketch
points are owned by the drawing work, but only if the drawing document
is active.

If the owning sketch of a sketch point is active,
or inactive, when the sketch point is obtained, then it must also be active,
or inactive, to deselect it. For example, if the owning sketch of a sketch
point is active when the sketch point is obtained, then the owning sketch
must be active to select or deselect the sketch point. Likewise, if the
owning sketch of a sketch point is inactive when the sketchpoint is obtained,
then the owning sketch must be inactive to select or deselect the sketchpoint

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SketchPoint_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SketchPoint\SketchPoint__Select.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
