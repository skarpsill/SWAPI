---
title: "ModelDoc::InsertNote"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertNote.htm"
---

# ModelDoc::InsertNote

This
method is obsolete and has been superseded by[ModelDoc2::InsertNote](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertNote.htm).

Description

This method creates a new note in this document.

Syntax (OLE Automation)

retval = ModelDoc.InsertNote (text)

(Table)=========================================================

| Input: | ( BSTR ) text | T ext string or symbol to be put
in the note |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the new Note object |

Syntax (COM)

status = ModelDoc->IInsertNote ( text, &retval
)

(Table)=========================================================

| Input: | (BSTR) text | T ext string or symbol to be put
in the note |
| --- | --- | --- |
| Output: | (LPNOTE) retval | Pointer to the new Note object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The leader attachment points for the note that
is created come from the selections made before calling this method. The
initial location of the note will also be near the selection location.
If there are no selections, the note will not have a leader, be free standing,
and initially be at the origin of the model or drawing.

This method creates a default note. To adjust the
display characteristics of this note, you should use the pointer that
is returned by this method to access the various properties and get and
set methods of the Note interface, such as Note::SetBalloon and Note::Angle.
Use the Note::GetAnnotation method to retrieve the Annotation object,
which has other useful methods, such as Annotation::SetLeader2 and Annotation::SetPosition.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__InsertNote.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
