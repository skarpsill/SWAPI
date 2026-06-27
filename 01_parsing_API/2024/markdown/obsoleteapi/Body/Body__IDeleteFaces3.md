---
title: "Body::IDeleteFaces3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__IDeleteFaces3.htm"
---

# Body::IDeleteFaces3

This method is obsolete and has been superseded by[Body2::IDeleteFaces3](sldworksAPI.chm::/Body2/Body2__IDeleteFaces3.htm).

Description

This method deletes a set of faces from a temporary body.

Syntax (OLE Automation)

Not available.

Syntax
(COM)

status = Body->IDeleteFaces3 ( nFaces,
facesToDelete, healOption, doLocalCheck, &retval )

(Table)=========================================================

| Input: | (int) nFaces | Number of faces to use for body creation |
| --- | --- | --- |
| Input: | (LPFACE)* facesToDelete | Array containing the faces for deletion |
| Input: | (int) healOption | Additional control |
| Input: | (VARIANT_BOOL) doLocalCheck | TRUE checks the bodies during the operation and sets retval to indicate
whether or not the resultant body is valid |
| Output: | (VARIANT_BOOL) retval | TRUE if body is valid, FALSE if it is not. To obtain this value, you
must pass TRUE for the doLocalCheck argument |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE if the operation fails to complete or the
faces do not belong to the body |

Remarks

All of the specified faces, which must belong to
this temporary body, are deleted from the body. If the resulting body
does not have a complete boundary, then SolidWorks treats any holes as
wounds which are healed as specified by the healOption argument. The healOption
argument can take the following values:

(Table)=========================================================

| Value | Loops on the faces to be deleted are... |
| --- | --- |
| 0 | Dependent on each other and healed at the same time. If extending faces
does not yield a solution, then shrinking the faces is tried. |
| 1 | Independent and healed separately. This option also grows the faces
the parent had around the hole to cover the hole. |
| 2 | Independent and healed separately. This option also finds a surface
in which all edges of a hole lie and attach this to a face covering the
hole (SolidWorks creates a new face to cover the hole). |

For example, consider a cube with a through hole
made up of four faces (a square hole). To delete these four faces, specify
option 0 because the loop on the first face to be deleted is dependent
on the loop of the second face to be deleted. Likewise, the loop on the
second face to be deleted is dependent on the third face to be deleted,
and so on.

Now consider the same cube with a through hole,
except this through hole is a simple cylinder ( one face). To delete the
cylindrical face, specify option 1 because it heals the loops independently.
This is necessary because the cylindrical face actually has two loops
(one at either end of the cylinder) that need to be healed separately.

If you choose not to use the doLocalCheck option, you can also check
the body validity after the operation using the Body::Check function.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$ZModifyFace$$**$$ZModifyBody$$**$$ZDeleting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Body\Body__IDeleteFaces3.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
