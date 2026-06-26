---
title: "ModelDoc::InsertObjectFromFile"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertObjectFromFile.htm"
---

# ModelDoc::InsertObjectFromFile

This
method is obsolete and has been superseded by[ModelDoc2::InsertObjectFromFile](../ModelDoc2/ModelDoc2__InsertObjectFromFile.htm).

Description

This method adds an OLE object from a specified
file and inserts it at the location specified.

Syntax (OLE Automation)

retval = ModelDoc.InsertObjectFromFile (filePath, createLink, x, y, z)

(Table)=========================================================

| Input: | (BSTR) filePath | Full path name to the file being inserted |
| --- | --- | --- |
| Input: | (BOOL) createLink | TRUE to create a link to the file, FALSE to embed
the file |
| Input: | (double) x | X component of the location to insert the object |
| Input: | (double) y | Y component of the location to insert the object |
| Input: | (double) z | Z component of the location to insert the object |
| Return: | (BOOL) retval | TRUE if the operation was successful, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertObjectFromFile ( filePath,
createLink, x, y, z, &retval )

(Table)=========================================================

| Input: | (BSTR) filePath | Full path name to the file being inserted |
| --- | --- | --- |
| Input: | (BOOL) createLink | TRUE to create a link to the file, FALSE to embed
the file |
| Input: | (double) x | X component of the location to insert the object |
| Input: | (double) y | Y component of the location to insert the object |
| Input: | (double) z | Z component of the location to insert the object |
| Output: | (VARIANT_BOOL) retval | TRUE if the operation was successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Currently, only the DrawingDoc object uses the
x,y,z coordinate position. The PartDoc and AssemblyDoc objects place the
inserted object at the upper-right hand corner of the ModelView object.

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
<param name="Items" value="ModelDoc Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\ModelDoc\ModelDoc__InsertObjectFromFile.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
