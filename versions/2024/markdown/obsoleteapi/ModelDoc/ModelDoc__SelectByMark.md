---
title: "ModelDoc::SelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectByMark.htm"
---

# ModelDoc::SelectByMark

This method is obsolete
and has been superseded by[ModelDoc2::SelectByMark](../ModelDoc2/ModelDoc2__SelectByMark.htm).

Description

This methodkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}and
ModelDoc::AndSelectByMark behave exactly the same as ModelDoc::SelectById
and ModelDoc::AndSelectById, except that the former methods mark the selected
entity with the integer mark provided as the last argument. This mark
is used by API functions that require multiple selections.

Syntax (OLE Automation)

retval = ModelDoc.SelectByMark ( selID,
selParams, x, y, z, mark)

(Table)=========================================================

| Input: | (BSTR) selID | ID of object; this case-sensitive string is intended for objects that
are automatically named by SolidWorks during entity creation, such as
dimensions and drawing views; if you do not know the object ID or if it
is an item that is not automatically named by SolidWorks, you can pass
an empty string |
| --- | --- | --- |
| Input: | (BSTR) selParams | Uppercase type name of object (for exmample, "EDGE"); see
swSelectType_e for valid names; if you do not know the object type, you
can pass in an empty string |
| Input: | (double) x | X selection location; values are in meters; in certain situations you
can simply pass in ( 0,0,0 ); see ModelDoc::SelectByID for details |
| Input: | (double) y | Y selection location; values
are in meters; in certain situations you can simply pass in ( 0,0,0 );
see ModelDoc::SelectByID for details |
| Input: | (double) z | Z selection location; values
are in meters; in certain situations you can simply pass in ( 0,0,0 );
see ModelDoc::SelectByID for details |
| Input: | (long) mark | Number to use as a mark |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SelectByMark
( selID, selParams, x, y, z, mark, &retval )

(Table)=========================================================

| Input: | (BSTR) selID | ID of object; this case-sensitive string is intended for objects that
are automatically named by SolidWorks during entity creation, such as
dimensions and drawing views; if you do not know the object ID or if it
is an item that is not automatically named by SolidWorks, you can pass
an empty string |
| --- | --- | --- |
| Input: | (BSTR) selParams | Uppercase type name of object (for example, "EDGE"); see swSelectType_e
for valid names; if you do not know the object type, you can pass in an
empty string |
| Input: | (double) x | X selection location; values are in meters; in certain situations you
can pass in ( 0,0,0 ); see ModelDoc::SelectByID for details |
| Input: | (double) y | Y selection location; values
are in meters; in certain situations you can pass in ( 0,0,0 ); see ModelDoc::SelectByID
for details |
| Input: | (double) z | Z selection location; values
are in meters; in certain situations you can pass in ( 0,0,0 ); see ModelDoc::SelectByID
for details |
| Input: | (long) mark | The number to use as a mark |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SelectByMark.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
