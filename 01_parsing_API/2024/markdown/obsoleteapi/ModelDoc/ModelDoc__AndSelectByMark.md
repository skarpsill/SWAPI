---
title: "ModelDoc::AndSelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AndSelectByMark.htm"
---

# ModelDoc::AndSelectByMark

This
method is obsolete and has been superseded by[ModelDoc2::AndSelectByMark](../ModelDoc2/ModelDoc2__AndSelectByMark.htm).

Description

This method adds an object to the selections, or removes it if it is
already selected. The selection is added with a mark as required by certain
API functions that use multiple selections. For a full description of
the arguments ,see ModelDoc::SelectByMark

Syntax (OLE Automation)

retval = ModelDoc.AndSelectByMark (
selID, selParams, x, y, z, mark)

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

status = ModelDoc->AndSelectByMark
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
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="13160660" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="ModelDoc_Object$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__AndSelectByMark.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
