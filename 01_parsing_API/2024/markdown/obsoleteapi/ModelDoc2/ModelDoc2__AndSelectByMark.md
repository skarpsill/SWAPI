---
title: "ModelDoc2::AndSelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AndSelectByMark.htm"
---

# ModelDoc2::AndSelectByMark

This
method is obsolete and has been superseded by ModelDocExtension::SelectByID .

Description

This method adds an object to the selections or removes it if it is
already selected. The selection is added with a mark as required by certain
API functions that use multiple selections, such as ModelDoc2::InsertMfDraft,
ModelDoc2::InsertSplitLineSil, and ModelDoc2::InsertSplitLineProject.

Syntax (OLE Automation)

retval = ModelDoc2.AndSelectByMark
( selID, selParams, x, y, z, mark)

(Table)=========================================================

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object |
| Input: | (double) x | X selection location |
| Input: | (double) y | Z selection location |
| Input: | (double) z | Z selection location |
| Input: | (long) mark | Number you wish to use as a mark |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->AndSelectByMark
( selID, selParams, x, y, z, mark, &retval )

(Table)=========================================================

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object |
| Input: | (double) x | X selection location |
| Input: | (double) y | Z selection location |
| Input: | (double) z | Z selection location |
| Input: | (long) mark | Number you wish to use as a mark |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method instead of using the individual
selection methods on the following objects:

- Annotation
- Component2
- Feature
- SketchHatch
- SketchPoint
- SketchSegment

The previously listed objects' selection methods
do not work well when a PropertyManager page is open or a command is running.
This method, ModelDoc2::AndSelectByMark, handles selection correctly whether
or not a command is running.

If you specify a mark, SolidWorks puts the selection
into the selection list box that has that mark, regardless of whether
it is active or not. If you do not specify a mark, SolidWorks puts the
selection into the active selection list box. Keep in mind that the selection
still has to pass the entity filtering criteria for that selection list
box before SolidWorks adds it completely.

If you want SolidWorks to mark your entity, pass
0 as the mark argument.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\ModelDoc2\ModelDoc2__AndSelectByMark.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\ModelDoc2\ModelDoc2__AndSelectByMark.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
