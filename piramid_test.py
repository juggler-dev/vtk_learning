# # Define Points: A pyramid needs five points (four for the base, one for the tip).
# # vtkPyramid: Defines the pyramid shape by connecting these points.
# # vtkUnstructuredGrid: Stores the points and the pyramid cell.
# # vtkDataSetMapper: Maps the unstructured grid to a renderable object.
# # vtkActor: Represents the pyramid in the 3D scene.
# # vtkRenderer & vtkRenderWindow: Handles rendering.
# # vtkRenderWindowInteractor: Enables user interaction.

import vtk

# Define points for the pyramid (base is a square, top is a single point)
points = vtk.vtkPoints()
points.InsertNextPoint(0, 0, 0)  # Base bottom-left
points.InsertNextPoint(1, 0, 0)  # Base bottom-right
points.InsertNextPoint(1, 1, 0)  # Base top-right
points.InsertNextPoint(0, 1, 0)  # Base top-left
points.InsertNextPoint(0.5, 0.5, 1)  # Apex (top point)

# Create a VTK pyramid
pyramid = vtk.vtkPyramid()
pyramid.GetPointIds().SetId(0, 0)
pyramid.GetPointIds().SetId(1, 1)
pyramid.GetPointIds().SetId(2, 2)
pyramid.GetPointIds().SetId(3, 3)
pyramid.GetPointIds().SetId(4, 4)

# Create a cell array to store the pyramid
cells = vtk.vtkCellArray()
cells.InsertNextCell(pyramid)

# Create a polydata object
polydata = vtk.vtkUnstructuredGrid()
polydata.SetPoints(points)
polydata.InsertNextCell(pyramid.GetCellType(), pyramid.GetPointIds())

# Create a mapper
mapper = vtk.vtkDataSetMapper()
mapper.SetInputData(polydata)

# Create an actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1.0, 0.6, 0.2)  # Orange color

# Create a renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.2, 0.2, 0.2)

# Create a render window
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(600, 600)

# Create an interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Start rendering
render_window.Render()
interactor.Start()
