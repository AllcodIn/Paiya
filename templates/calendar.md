<!DOCTYPE html>

<html lang="fr">

<head>

  <meta charset="UTF-8">

  <title>Calendrier de gestion d'événements</title>

  <link href="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.5/main.min.css" rel="stylesheet">

  <script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.5/main.min.js"></script>

  <style>

    #calendar {

      max-width: 900px;

      margin: 50px auto;

    }

  </style>

</head>

<body>

  <div id="calendar"></div>

  <script>

    document.addEventListener('DOMContentLoaded', function () {

      const calendarEl = document.getElementById('calendar');

      const calendar = new FullCalendar.Calendar(calendarEl, {

        initialView: 'dayGridMonth', // Vue mensuelle

        editable: true,             // Permet le glisser-déposer

        events: [                   // Exemple d'événements

          { title: 'Réunion', start: '2025-01-10' },

          { title: 'Conférence', start: '2025-01-15', end: '2025-01-17' },

          { title: 'Anniversaire', start: '2025-01-20' },

        ],

        headerToolbar: {

          left: 'prev,next today',

          center: 'title',

          right: 'dayGridMonth,timeGridWeek,timeGridDay'

        },

      });

      calendar.render();

    });

  </script>

</body>

</html>